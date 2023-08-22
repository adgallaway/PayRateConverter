import configparser
import estTax

def case(frequency, selection, pay): # Decide which Calculations to Perform
    config = configparser.ConfigParser()
    config.read('settings.ini')
    frequency = int(frequency)
    msg_text = []
    hours_daily = float(config['WORK.WEEK']['hours'])
    days_weekly = int(config['WORK.WEEK']['days'])
    work_week = hours_daily * days_weekly

    def hourly(): #Perform Calculation for Hourly Pay
        match frequency:
            case 1: hourlyPay = float(pay)                              # Paid Hourly
            case 2: hourlyPay = float(pay / work_week)                  # Paid Weekly
            case 3: hourlyPay = float(pay / (work_week * 2))            # Paid Bi-Weekly
            case 4: hourlyPay = float(((pay * 24) / 52) / work_week)    # Paid Semi-Montly
            case 5: hourlyPay = float(((pay * 12) / 52) / work_week)    # Paid Monthly
            case 6: hourlyPay =float((pay / 52) / work_week)            # Paid Annually
        text = "Estimated Hourly pay:"
        taxed = estTax.tax(hourlyPay)
        tup = (text, hourlyPay, taxed)
        msg_text.append(tup)

    def weekly(): #Perform Calculation for Weekly Pay
        match frequency:
            case 1: weeklyPay = float(pay * work_week)  # Paid Hourly
            case 2: weeklyPay = float(pay)              # Paid Weekly
            case 3: weeklyPay = float(pay / 2)          # Paid Bi-Weekly
            case 4: weeklyPay = float((pay * 24) / 52)  # Paid Semi-Montly
            case 5: weeklyPay = float((pay * 12) / 52)  # Paid Monthly
            case 6: weeklyPay =float(pay / 52)          # Paid Annually
        text = "Estimated Weekly pay:"
        taxed = estTax.tax(weeklyPay)
        tup = (text, weeklyPay, taxed)
        msg_text.append(tup)

    def biweekly(): #Perform Calculation for Bi-Weekly Pay
        match frequency:
            case 1: biWeeklyPay = float(pay * (work_week * 2))  # Paid Hourly
            case 2: biWeeklyPay = float(pay * 2)                # Paid Weekly
            case 3: biWeeklyPay = float(pay)                    # Paid Bi-Weekly
            case 4: biWeeklyPay = float(((pay * 24) / 52) * 2)  # Paid Semi-Montly
            case 5: biWeeklyPay = float(((pay * 12) / 52) * 2)  # Paid Monthly
            case 6: biWeeklyPay =float((pay / 52) * 2)          # Paid Annually
        text = "Estimated Bi-Weekly pay:"
        taxed = estTax.tax(biWeeklyPay)
        tup = (text, biWeeklyPay, taxed)
        msg_text.append(tup)

    def semimonthly(): #Perform Calculation for Monthly Pay
        match frequency:
            case 1: semimonthlypay = float(((pay * work_week) * 52) / 24)   # Paid Hourly
            case 2: semimonthlypay = float((pay * 52) / 24)                 # Paid Weekly
            case 3: semimonthlypay = float((pay * 26) / 24)                 # Paid Bi-Weekly
            case 4: semimonthlypay = float(pay)                             # Paid Semi-Montly
            case 5: semimonthlypay = float(pay / 2)                         # Paid Monthly
            case 6: semimonthlypay = float(pay / 24)                        # Paid Annually
        text = "Estimated Semi-Monthly pay:"
        taxed = estTax.tax(semimonthlypay)
        tup = (text, semimonthlypay, taxed)
        msg_text.append(tup)

    def monthly(): #Perform Calculation for Monthly Pay
        match frequency:
            case 1: monthlyPay = float(((pay * work_week) * 52) / 12)   # Paid Hourly
            case 2: monthlyPay = float((pay * 52) / 12)                 # Paid Weekly
            case 3: monthlyPay = float((pay * 26) / 12)                 # Paid Bi-Weekly
            case 4: monthlyPay = float(pay * 2)                         # Paid Semi-Montly
            case 5: monthlyPay = float(pay)                             # Paid Monthly
            case 6: monthlyPay = float(pay / 12)                        # Paid Annually
        text = "Estimated Monthly pay:"
        taxed = estTax.tax(monthlyPay)
        tup = (text, monthlyPay, taxed)
        msg_text.append(tup)

    def annually(): #Perform Calculation for Annual Pay
        match frequency:
            case 1: annualPay = float((pay * work_week) * 52)   # Paid Hourly
            case 2: annualPay = float(pay * 52)                 # Paid Weekly
            case 3: annualPay = float(pay * 26)                 # Paid Bi-Weekly
            case 4: annualPay = float(pay * 24)                 # Paid Semi-Montly
            case 5: annualPay = float(pay * 12)                 # Paid Monthly
            case 6: annualPay = float(pay)                      # Paid Annually
        text = "Estimated Annual pay:"
        taxed = estTax.tax(annualPay)
        tup = (text, annualPay, taxed)
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


