from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import *
import datetime
from django.views.generic import  UpdateView, DeleteView
from .tasks import datagenerate


def load(request):
    task = go_to_sleep.delay(1)
    return render(request, 'load.html', {'task_id': task.task_id})


def home_view(request):
    user = request.user
    schemes = Scheme.objects.filter(author=user)
    return render(request, 'home.html', {'schemes':schemes})


def generate_view(request):
    user = request.user
    schemes = Scheme.objects.filter(author=user)
    return render(request, 'generate.html', {'schemes':schemes})



def scheme_create(request):  
    form = SchemeForm()  
    if request.method == 'POST':
        form = SchemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')        

    return render(request, 'scheme.html', {'form': form})



class SchemeEditView(UpdateView):
    template_name = "scheme-edit.html"
    form_class = SchemeForm
    success_url = '/home/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Scheme, id=id_)


class SchemeDeleteView(DeleteView):
    template_name = "scheme-delete.html"
    success_url = '/home/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Scheme, id=id_)

    def get_success_url(self):
        return "/home/"


def do(request, id=None):
    # Get scheme
    scheme = Scheme.objects.get(id=id)
    scheme_id = int(scheme.id)
    print(scheme)
    print(scheme.id)
    print(int(scheme.id))

    # COLUMNS
    # Get columns
    columns = []

    columns.append(scheme.type1)
    columns.append(scheme.type2)
    columns.append(scheme.type3)
    columns.append(scheme.type4)
    columns.append(scheme.type5)
    columns.append(scheme.type6)

    # Replace IDs with names
    col_names = {'1': 'Choose...',
                 '2': 'name',
                 '3': 'job',
                 '4': 'company',
                 '5': 'phone',
                 '6': 'address',
                 '7': 'email', }

    def replace(list, dictionary):
        for idx, val in enumerate(list):
            list[idx] = dictionary[list[idx]]
        return list
    replace(columns, col_names)
    while 'Choose...' in columns:
        columns.remove('Choose...')

    print ('Columns: ')
    print(columns)

    # NAMES
    # Get names
    names = []

    names.append(scheme.col_name1)
    names.append(scheme.col_name2)
    names.append(scheme.col_name3)
    names.append(scheme.col_name4)
    names.append(scheme.col_name5)
    names.append(scheme.col_name6)

    while '' in names:
        names.remove('')

    while 'None' in names:
        names.remove('None')

    print('Names of columns: ')
    print(names)

    # ORDER
    # Get order
    order = []

    order.append(scheme.order1)
    order.append(scheme.order2)
    order.append(scheme.order3)
    order.append(scheme.order4)
    order.append(scheme.order5)
    order.append(scheme.order6)

    while 0 in order:
        order.remove(0)

    print('Order: ')
    print(order)

    if order:
        columns = [x for _, x in sorted(zip(order, columns))]
        names = [x for _, x in sorted(zip(order, names))]

    print('Columns in order: ')
    print(columns)
    print(names)

    rows = scheme.rows
    print('Number of rows:')
    print(rows)

    filename = str(scheme.author) + '_' + str(scheme.name) + '_' + str(datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'

    task = datagenerate.delay(rows, columns, names, filename, scheme_id)
    print(filename)

    return render(request, 'load.html', {'task_id': task.task_id})

