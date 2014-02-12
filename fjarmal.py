from bottle import route, run, template, post, request, static_file
from Loan import *

@route('/')
def index():
    return template('main')

@route('/spara', method='POST')
def form():
    amount = request.forms.getall('time')
    return amount

@route('/lan', method='POST')
def form():

    #Period for saving/paying into loan
    periodYears = int(request.forms.get('periodYears'))
    periodMonths = int(request.forms.get('periodMonths'))
    totalPeriod = ( periodYears * 12 ) + periodMonths

    #amount the user has leftover
    monthlyAmount = int(request.forms.get('monthlyAmount'))

    #inflation period
    inflateYstart = request.forms.get('inflYstart')
    inflateMstart = request.forms.get('inflMstart')
    inflateYend = request.forms.get('inflYend')
    inflateMend = request.forms.get('inflMend')
    inflPeriodStartKey = inflateYstart + "-" + inflateMstart
    inflPeriodEndKey = inflateYend + "-" + inflateMend

    #we're using .getall so these are lists
    name = request.forms.getall('lname')
    principle = request.forms.getall('principle')
    i_rate = request.forms.getall('i_rate')
    term = request.forms.getall('term')
    comp_freq = request.forms.getall('compoundInt')
    indexed = request.forms.getall('indexed')
    loans = []

    #we assume all the lists are equally long, iterate over them and create a list of loans
    #loans.append( Loan( name[i], float(principle[i]), float(i_rate[i]), int(term[i]), int(comp_freq[i]), False ) )

    for i in range(0, len(principle)):
        loans.append( Loan( name[i], float(principle[i]), float(i_rate[i]), int(term[i]), int(comp_freq[i]), False ) )

    #loans.append( Loan( "nafn", 3000000, 4, 24, 12, True ) )

    res = evaluate(loans, totalPeriod, monthlyAmount)

    return template('results', loanList=res)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080)