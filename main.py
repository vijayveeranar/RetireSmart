import locale

current_age = 40
retirement_age = 50
# term_suggestion = ""
exp_monthly_income_ret = 0
rental_income_ret = 0
monthly_pension_ret = 0
monthly_rent = 20000
curr_asset = 0
term_insurance_cov_per_rs = 8000
health_insurance_cov_per_rs = 33.33
other_suggestion = ""
health_suggestion = ""
# Set the locale to Indian English
locale.setlocale(locale.LC_ALL, 'en_IN')
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def check_term_cover(term_ins_cover, savings_amount, min_term_cover):
    if(term_ins_cover >= min_term_cover):
        term_deficit = 0
        term_suggestion = "You've wisely secured sufficient term insurance coverage"
    else:
        term_deficit = min_term_cover - term_ins_cover
        mon_premium = term_deficit / term_insurance_cov_per_rs
        if(savings_amount >= mon_premium):
            
            formatted_term_deficit = locale.currency(term_deficit, grouping=True)
            formatted_savings_amount = locale.currency(savings_amount, grouping=True)
            formatted_mon_premium = locale.currency(mon_premium, grouping=True)
            term_suggestion = f"You are left with {formatted_savings_amount} to Invest. To ensure the safety and well-being of your family in any unfortunate event, it is advisable to obtain an additional term cover of {formatted_term_deficit} as a monthly premium {formatted_mon_premium}"
            savings_amount = savings_amount - mon_premium
        else:
            formatted_savings_amount = locale.currency(savings_amount, grouping=True)
            term_suggestion = f"You are left with only {formatted_savings_amount} to Invest. No savings possible due to financial constraints. Improve financial situation: Upskill for better job or reduce expenses."
    return term_suggestion, savings_amount

def check_health_cover(health_ins_cover, savings_amount, min_health_cover):
    if(health_ins_cover >= min_health_cover):
        health_deficit = 0
        health_suggestion = "Your wise choice to secure a significant health cover is commendable. Keep investing in it annually for continuous protection."
    else:
        health_deficit = min_health_cover - health_ins_cover
        mon_premium = health_deficit/health_insurance_cov_per_rs
        if(savings_amount >= mon_premium):
            formatted_health_deficit = locale.currency(health_deficit, grouping=True)
            formatted_savings_amount = locale.currency(savings_amount, grouping=True)
            formatted_mon_premium = locale.currency(mon_premium, grouping=True)
            health_suggestion = f"After making above investments you are left with {formatted_savings_amount} to Invest.Consider acquiring an additional health insurance cover of {formatted_health_deficit} at a monthly premium {formatted_mon_premium} for the utmost protection and well-being of your family "
            savings_amount = savings_amount - mon_premium
        else:
            formatted_savings_amount = locale.currency(savings_amount, grouping=True)
            health_suggestion = f"You are left with only {formatted_savings_amount} to Invest. No savings possible due to financial constraints. Improve financial situation: Upskill for better job or reduce expenses."
    return health_suggestion, savings_amount

def check_emergency_cover(emergency_fund, savings_amount, min_emergency_cover):
    if(emergency_fund >= min_emergency_cover):
        emergency_deficit = 0
        emergency_suggestion = "You have prudently accumulated a substantial emergency fund, providing you with a strong financial safeguard."
    else:
        emergency_deficit = min_emergency_cover - emergency_fund
        emergency_fund_mon = emergency_deficit/36
        emergency_fund_mon = min(emergency_fund_mon, savings_amount)
        formatted_emergency_deficit = locale.currency(emergency_deficit, grouping=True)
        formatted_emergency_fund_mon = locale.currency(round(emergency_fund_mon), grouping=True)
        emergency_suggestion = f"Ensure financial stability by building an emergency fund of {formatted_emergency_deficit} in next 3 years through monthly fixed depsoit investments of {formatted_emergency_fund_mon}"
        savings_amount = savings_amount - emergency_fund_mon

    return emergency_suggestion, savings_amount

    

def save_your_today(term_ins_cover, health_ins_cover, emergency_fund, savings_amount, \
                    min_term_cover, min_health_cover, min_emergency_cover):
    term_suggestion, savings_amount = check_term_cover(term_ins_cover, savings_amount, min_term_cover)
    if(savings_amount >= 500):
        health_suggestion, savings_amount = check_health_cover(health_ins_cover, savings_amount, min_health_cover)
    if(savings_amount >= 500):
        emergency_suggestion, savings_amount = check_emergency_cover(emergency_fund, savings_amount, min_emergency_cover)
    return term_suggestion, health_suggestion, emergency_suggestion, savings_amount

def calculate_monthly_investment_return(monthly_investment, annual_return_rate, years):
    # Convert the annual return rate to decimal form
    rate = annual_return_rate / 100

    # Calculate the number of total months
    total_months = years * 12

    # Calculate the final amount using the monthly investment and compound interest formula
    final_amount = 0
    for month in range(1, total_months + 1):
        final_amount += monthly_investment
        final_amount *= (1 + rate/12)

    return final_amount

def plan_for_tomorrow(average_income_mon, savings_amount, years_to_retire, annual_return_rate):
    corpus_for_retire = 0
    if(savings_amount < 1000):
        formatted_savings_amount = locale.currency(savings_amount, grouping=True)
        surplus_suggestion = f"After making above investments you are left with {formatted_savings_amount} to Invest.No further savings possible due to financial constraints. Fix the Basics listed above first. Improve financial situation: Upskill for better job or reduce expenses."
        
    elif((savings_amount/average_income_mon)>0.2) :
        mutual_premium_mon = average_income_mon * 0.2
        savings_amount = savings_amount - mutual_premium_mon
        high_risk_alloc = mutual_premium_mon * 0.10
        medium_risk_alloc = mutual_premium_mon * 0.25
        low_risk_alloc = mutual_premium_mon * 0.65
        formatted_high_risk_alloc = locale.currency(high_risk_alloc, grouping=True)
        formatted_medium_risk_alloc = locale.currency(medium_risk_alloc, grouping=True)
        formatted_low_risk_alloc = locale.currency(low_risk_alloc, grouping=True)
        surplus_suggestion = f"On a monthly basis, allocate {formatted_low_risk_alloc} to low-risk mutual funds (such as Nifty), {formatted_medium_risk_alloc} rs to medium-risk mutual funds (sectoral/mid-cap), and {formatted_high_risk_alloc} rs to high-risk mutual funds (like small-cap)."
        corpus_for_retire = calculate_monthly_investment_return(mutual_premium_mon, annual_return_rate, years_to_retire)

    else:
        high_risk_alloc = savings_amount * 0.10
        medium_risk_alloc = savings_amount * 0.25
        low_risk_alloc = savings_amount * 0.65
        formatted_high_risk_alloc = locale.currency(high_risk_alloc, grouping=True)
        formatted_medium_risk_alloc = locale.currency(medium_risk_alloc, grouping=True)
        formatted_low_risk_alloc = locale.currency(low_risk_alloc, grouping=True)
        surplus_suggestion = f"On a monthly basis, allocate {formatted_low_risk_alloc} rs to low-risk mutual funds (such as Nifty), {formatted_medium_risk_alloc} rs to medium-risk mutual funds (sectoral/mid-cap), and {formatted_high_risk_alloc} rs to high-risk mutual funds (like small-cap)."
        corpus_for_retire = calculate_monthly_investment_return(savings_amount, annual_return_rate, years_to_retire)
        savings_amount = 0
    return surplus_suggestion, savings_amount, corpus_for_retire

def more_for_retire(savings_amount, monthly_rent, years_to_retire, annual_return_rate, corpus_for_retire):
    if(monthly_rent > 10000 and savings_amount >= (3*monthly_rent)):
        other_suggestion = "Eliminate monthly rental expense by purchasing a house."
    else:
        formatted_savings_amount = locale.currency(round(savings_amount,0), grouping=True)
        other_suggestion = f"Consider investing {formatted_savings_amount} to investment options such as gold, real estate, or bonds."
        more_return = calculate_monthly_investment_return(savings_amount, annual_return_rate, years_to_retire)
        corpus_for_retire = corpus_for_retire + more_return
    return other_suggestion, corpus_for_retire

def calculate_corpus_for_monthly_income(monthly_income, annual_return_rate):
    # Convert the annual return rate to decimal form
    rate = annual_return_rate / 100

    # Calculate the monthly return rate
    monthly_return_rate = rate / 12

    # Calculate the corpus required using the formula:
    # Corpus = Monthly Income / Monthly Return Rate
    corpus = monthly_income / monthly_return_rate

    return corpus
def calculate_monthly_interest(principal, annual_interest_rate):
    monthly_interest_rate = (annual_interest_rate*0.01) / 12
    monthly_interest_amount = principal * monthly_interest_rate
    return monthly_interest_amount


def retirement_readiness(corpus_for_retire, monthly_income_post_ret, annual_return_rate, rental_income_ret, \
                         monthly_pension_ret, curr_asset) :
    dilution_suggestion = ""
    monthly_income_post_ret = monthly_income_post_ret - (monthly_pension_ret + rental_income_ret)
    req_corpus_for_ret = calculate_corpus_for_monthly_income(monthly_income_post_ret, annual_return_rate)
    readiness = corpus_for_retire / req_corpus_for_ret
    if(readiness < 1 and curr_asset > 50000):
        dilution_of_assets_req = min(req_corpus_for_ret, curr_asset)
        # you need to exclude rental and recaculate the need for additional corpus because mostly you will dilute the rent generating asset
        # rental_impact = dilution_of_assets_req * 0.0025
        # rental_income_ret = max(0, rental_income_ret - rental_impact)
        # additional_dilution_needed = calculate_corpus_for_monthly_income(rental_impact, annual_return_rate)
        # dilution_of_assets_req = min(dilution_of_assets_req +  additional_dilution_needed, curr_asset)
        formatted_dilution_of_assets_req = locale.currency(round(dilution_of_assets_req,0), grouping=True)
        formatted_corpus_for_retire = locale.currency(round(corpus_for_retire,0), grouping=True)
        dilution_suggestion = f"When you approach retirement age, it is advisable to dilute your assets and distribute the proceeds of {formatted_dilution_of_assets_req} to buy monthly income plans like (POMIS, SWP, MIP). Additionally, you can utilize the funds accumulated from your investments, amounting to {formatted_corpus_for_retire}, and allocate them towards annuity plans as you near retirement."
        corpus_for_retire = corpus_for_retire + dilution_of_assets_req
        readiness = corpus_for_retire / req_corpus_for_ret

    if(readiness >= 1):
        readiness = 100
        readiness_suggestion = f"Excellent your retirment readiness based on suggested plan is {readiness} %! Continue investing based on above suggestion and you are on your way to a wonderful retirment"
    else:
        readiness = round(readiness * 100)
        readiness_suggestion = f"if you go by the suggested plan above then you are {readiness} % ready for your retirement. To increase readiness consider increasing our income or reduce expenses"
    annuity_mon_ret = calculate_monthly_interest(corpus_for_retire, annual_return_rate)
    tot_mon_income = monthly_pension_ret + rental_income_ret + annuity_mon_ret
    formatted_monthly_pension_ret = locale.currency(round(monthly_pension_ret,0), grouping=True)
    formatted_rental_income_ret = locale.currency(round(rental_income_ret,0), grouping=True)
    formatted_annuity_mon_ret = locale.currency(round(annuity_mon_ret,0), grouping=True)
    formatted_tot_mon_income = locale.currency(round(tot_mon_income,0), grouping=True)
    summary = f"Upon retirement, you will begin receiving a monthly pension of {formatted_monthly_pension_ret}. In addition, you will have rental income of {formatted_rental_income_ret} from your properties. Furthermore, you can expect a monthly annuity pension of {formatted_annuity_mon_ret}. Altogether, your total monthly income will amount to {formatted_tot_mon_income}."
    return readiness, dilution_suggestion, readiness_suggestion, summary



def start_readiness(term_ins_cover, health_ins_cover, emergency_fund, average_income_mon, \
                    monthly_emi, monthly_expense, current_age, retirement_age, rental_income_ret, \
                        monthly_pension_ret, curr_asset, exp_monthly_income_ret):
    
    health_suggestion = ""
    emergency_suggestion = ""
    surplus_suggestion = ""
    other_suggestion = ""
    term_suggestion = ""
    dilution_suggestion = ""
    readiness_suggestion = ""
    summary = ""
    readiness = 0
    corpus_for_retire = 0
    savings_amount = average_income_mon - (monthly_expense + monthly_emi)
    min_term_cover = min((average_income_mon * 12 * 10), 20000000)
    min_health_cover = min(average_income_mon / 6, 500000)
    years_to_retire = retirement_age - current_age
    annual_return_rate = 8
    monthly_income_post_ret = exp_monthly_income_ret

    min_emergency_cover = 6*average_income_mon
    if(savings_amount >= 500):
        term_suggestion, health_suggestion, emergency_suggestion, savings_amount = \
            save_your_today(term_ins_cover, health_ins_cover, emergency_fund, savings_amount, min_term_cover, \
                            min_health_cover, min_emergency_cover)
    else:
        term_suggestion = f"Insufficient funds for savings! Increase income or reduce expenses. Secure basic insurance and emergency cover for present stability."
    
    if(savings_amount > 1000):
        surplus_suggestion, savings_amount, corpus_for_retire = plan_for_tomorrow(average_income_mon, savings_amount, years_to_retire, annual_return_rate)
    if(savings_amount > 1000):
        
        other_suggestion, corpus_for_retire = more_for_retire(savings_amount, monthly_rent, years_to_retire, annual_return_rate, corpus_for_retire)
    readiness, dilution_suggestion, readiness_suggestion, summary = retirement_readiness(corpus_for_retire, monthly_income_post_ret, \
                                                           annual_return_rate, rental_income_ret, \
                                                            monthly_pension_ret, curr_asset)
    return term_suggestion, health_suggestion, emergency_suggestion, surplus_suggestion, other_suggestion,readiness, dilution_suggestion, readiness_suggestion, summary

