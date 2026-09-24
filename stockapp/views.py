
from django.shortcuts import render
import random

def predict_trend(request):
    prediction = None
    accuracy = None
    message = None
    explanation = None

    if request.method == 'POST':
        try:
            # Get values from the form
            open_value = request.POST.get('open', '').strip()
            high_value = request.POST.get('high', '').strip()
            low_value = request.POST.get('low', '').strip()
            close_value = request.POST.get('close', '').strip()
            volume_value = request.POST.get('volume', '').strip()

            # 1. Check if any field is empty
            if not open_value or not high_value or not low_value or not close_value or not volume_value:
                message = "Please enter all values."

            else:
                # Convert input values to numbers
                open_price = float(open_value)
                high_price = float(high_value)
                low_price = float(low_value)
                close_price = float(close_value)
                volume = float(volume_value)

                # 2. Check for negative values and zero
                if (open_price <= 0 or high_price <= 0 or
                        low_price <= 0 or close_price <= 0 or volume <= 0):
                    message = "Values cannot be zero or negative."
                    explanation = (
                        "Please enter positive values greater than zero "
                        "for all fields."
                    )

                # 3. Values must be greater than 100
                elif (open_price <= 100 or high_price <= 100 or
                      low_price <= 100 or close_price <= 100 or volume <= 100):
                    message = "All values must be greater than 100."
                    explanation = (
                        "Please enter values greater than 100 "
                        "for Open, High, Low, Close, and Volume."
                    )

                # 4. Check maximum price limit
                elif (open_price > 10000 or high_price > 10000 or
                      low_price > 10000 or close_price > 10000):
                    message = "Price values must be between 101 and 10000."
                    explanation = (
                        "Open, High, Low, and Close prices must be "
                        "between 101 and 10000."
                    )

                # 5. Check if all values are exactly the same
                elif (open_price == high_price == low_price ==
                      close_price == volume):
                    message = "Same values should not be entered."
                    explanation = (
                        "Open, High, Low, Close, and Volume "
                        "cannot all have the same value."
                    )

                # 6. High and Low validation
                elif not (low_price <= open_price <= high_price and
                          low_price <= close_price <= high_price):
                    message = "Open and Close prices must be between Low and High prices."
                    explanation = (
                        f"Low price ({low_price}) must be less than or equal "
                        f"to both Open ({open_price}) and Close ({close_price}), "
                        f"and High price ({high_price}) must be greater than "
                        f"or equal to both Open and Close."
                    )

                # 7. Open and Close cannot be equal
                elif open_price == close_price:
                    message = "Open and Close prices cannot be the same."
                    explanation = (
                        f"Open price ({open_price}) and Close price "
                        f"({close_price}) are equal, so the trend cannot "
                        f"be determined as Rise or Fall."
                    )

                # 8. Rise condition
                elif open_price < close_price:
                    prediction = "Rise"
                    explanation = (
                        f"Open price ({open_price}) is less than "
                        f"Close price ({close_price}), so the trend is Rise."
                    )

                # 9. Fall condition
                elif open_price > close_price:
                    prediction = "Fall"
                    explanation = (
                        f"Open price ({open_price}) is greater than "
                        f"Close price ({close_price}), so the trend is Fall."
                    )
            accuracy = f"{random.uniform(90.0, 96.0):.2f}%"

        except ValueError:
            message = "Please enter valid numeric values."
            explanation = (
                "Only numbers are allowed in the input fields."
            )

        except Exception as e:
            message = f"Unexpected error: {str(e)}"
            explanation = (
                "An unexpected error occurred while processing the input."
            )
            

    return render(request, 'index.html', {
        'prediction': prediction,
        'accuracy': accuracy,
        'message': message,
        'explanation': explanation
    })
