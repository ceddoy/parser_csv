from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView, ListView

from parserapp.forms import CSVFileForm
from parserapp.models import Item
from parserapp.services import load_csv_file


class ItemCreateView(CreateView):
    form_class = CSVFileForm
    success_url = '/'
    template_name = 'parserapp/upload_csv_file.html'

    def form_valid(self, form):
        self.object = form.save()
        Item.objects.bulk_create(load_csv_file(self.object.file.file.name))
        return HttpResponseRedirect(self.get_success_url())


class ItemListView(ListView):
    model = Item
    template_name = 'parserapp/items_list.html'
    paginate_by = 100
