from django.shortcuts import redirect, render
from product.models import Product, Review
from product.forms import ReviewForm


def product(request, productID):
    review_count = Review.objects.filter(product=productID).count()
    product = Product.objects.get(pk=productID)
    score = product.score

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user_id = request.user
            new_review.product = product
            new_review.save()
            if product.score == 0.0:
                score_avg = float(request.POST['score'])
                product.score = score_avg
                product.save()
            else:
                score_avg = (score * float(review_count)  + float(request.POST['score']))/ float(review_count+1)
                product.score = score_avg
                product.save()
        return redirect('/product/'+str(productID))

    
    review_list = Review.objects.filter(product=productID).order_by('created_at').reverse()[:10]

    

    context = {
        'review_count' : review_count,
        'product' : product,
        'review_list' : review_list
    }
    return render(request,'product/index.html', context)


def productReview(request, productID):
    review_count = Review.objects.filter(product=productID).count()
    product = Product.objects.get(pk=productID)
    review_list = Review.objects.filter(product=productID).order_by('created_at').reverse()

    context = {
        'review_count':review_count,
        'review_list':review_list,
        'product':product,
    }
    return render(request,'product/review.html', context)

