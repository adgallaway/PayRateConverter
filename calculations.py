def case(frequency, selection, pay): # Decide which Calculations to Perform
    frequency = int(frequency)
    msg_text = []

    def hourly(): #Perform Calculation for Hourly Pay
        match frequency:
            case 1: hourlyPay = float(pay)                      # Paid Hourly
            case 2: hourlyPay = float(pay / 40)                 # Paid Weekly
            case 3: hourlyPay = float(pay / 80)                 # Paid Bi-Weekly
            case 4: hourlyPay = float(((pay * 24) / 52) / 40)   # Paid Semi-Montly
            case 5: hourlyPay = float(((pay * 12) / 52) / 40)   # Paid Monthly
            case 6: hourlyPay =float((pay / 52) / 40)           # Paid Annually
        text = "Estimated Hourly pay:"
        tup = (text, hourlyPay)
        msg_text.append(tup)

    def weekly(): #Perform Calculation for Weekly Pay
        match frequency:
            case 1: weeklyPay = float(pay * 40)         # Paid Hourly
            case 2: weeklyPay = float(pay)              # Paid Weekly
            case 3: weeklyPay = float(pay / 2)          # Paid Bi-Weekly
            case 4: weeklyPay = float((pay * 24) / 52)  # Paid Semi-Montly
            case 5: weeklyPay = float((pay * 12) / 52)  # Paid Monthly
            case 6: weeklyPay =float(pay / 52)          # Paid Annually
        text = "Estimated Weekly pay:"
        tup = (text, weeklyPay)
        msg_text.append(tup)

    def biweekly(): #Perform Calculation for Bi-Weekly Pay
        match frequency:
            case 1: biWeeklyPay = float(pay * 80)               # Paid Hourly
            case 2: biWeeklyPay = float(pay * 2)                # Paid Weekly
            case 3: biWeeklyPay = float(pay)                    # Paid Bi-Weekly
            case 4: biWeeklyPay = float(((pay * 24) / 52) * 2)  # Paid Semi-Montly
            case 5: biWeeklyPay = float(((pay * 12) / 52) * 2)  # Paid Monthly
            case 6: biWeeklyPay =float((pay / 52) * 2)          # Paid Annually
        text = "Estimated Bi-Weekly pay:"
        tup = (text, biWeeklyPay)
        msg_text.append(tup)

    def semimonthly(): #Perform Calculation for Monthly Pay
        match frequency:
            case 1: semimonthlypay = float(((pay * 40) * 52) / 24)  # Paid Hourly
            case 2: semimonthlypay = float((pay * 52) / 24)         # Paid Weekly
            case 3: semimonthlypay = float((pay * 26) / 24)         # Paid Bi-Weekly
            case 4: semimonthlypay = float(pay)                     # Paid Semi-Montly
            case 5: semimonthlypay = float(pay / 2)                 # Paid Monthly
            case 6: semimonthlypay = float(pay / 24)                # Paid Annually
        text = "Estimated Semi-Monthly pay:"
        tup = (text, semimonthlypay)
        msg_text.append(tup)

    def monthly(): #Perform Calculation for Monthly Pay
        match frequency:
            case 1: monthlyPay = float(((pay * 40) * 52) / 12)  # Paid Hourly
            case 2: monthlyPay = float((pay * 52) / 12)         # Paid Weekly
            case 3: monthlyPay = float((pay * 26) / 12)         # Paid Bi-Weekly
            case 4: monthlyPay = float(pay * 2)                 # Paid Semi-Montly
            case 5: monthlyPay = float(pay)                     # Paid Monthly
            case 6: monthlyPay = float(pay / 12)                # Paid Annually
        text = "Estimated Monthly pay:"
        tup = (text, monthlyPay)
        msg_text.append(tup)

    def annually(): #Perform Calculation for Annual Pay
        match frequency:
            case 1: annualPay = float((pay * 40) * 52)  # Paid Hourly
            case 2: annualPay = float(pay * 52)         # Paid Weekly
            case 3: annualPay = float(pay * 26)         # Paid Bi-Weekly
            case 4: annualPay = float(pay * 24)         # Paid Semi-Montly
            case 5: annualPay = float(pay * 12)         # Paid Monthly
            case 6: annualPay = float(pay)              # Paid Annually
        text = "Estimated Annual pay:"
        tup = (text, annualPay)
        msg_text.append(tup)

    
    match selection:
        case 0: #Perform All Calculations
            if frequency != 1: hourly()
            if frequency != 2: weekly()
            if frequency != 3: biweekly()
            if frequency != 4: semimonthly()
            if frequency != 5: monthly()
            if frequency != 6: annually()
        case 1: #Calculate Hourly Pay
            hourly()
        case 2: #Calculate Weekly Pay
            weekly()
        case 3: #Calculate Bi-Weekly Pay
            biweekly()
        case 4: #Calculate Monthly Pay
            semimonthly()
        case 5: #Calculate Monthly Pay
            monthly()
        case 6: #Calculate Annual Pay
            annually()
    return msg_text


