from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import CreateView

from parserapp.forms import CSVFileForm
from parserapp.models import Item
from parserapp.services import load_csv_file


class ItemCreateView(CreateView):
    form_class = CSVFileForm
    template_name = 'parserapp/upload_csv_file.html'

    def form_valid(self, form):
        self.object = form.save()
        new_data = Item.objects.bulk_create(load_csv_file(self.object.file.file.name))
        return render(self.request, 'parserapp/items_list.html', {'object_list': new_data})
