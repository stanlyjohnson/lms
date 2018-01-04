from django.core.management.base import BaseCommand
from ms.models import author, book

des = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

auth = [["Ruskin Bond",83,"Britain"], ["Chetan Bhagat",43,"India"], ["Arundhati Roy",56,"India"], ["R. K. Narayan",95,"India"]]

class Command (BaseCommand):
    arg =''
    help = 'populate the db'

    def populate (self):
        auth_iter = iter(auth)
        for i in range(4):
            aauth = next(auth_iter)
            aauth_iter = iter(aauth)
            aname = next(aauth_iter)
            print(aname)
            record = author(name = aname , age = next(aauth_iter) , country= next(aauth_iter) , about = des)
            record.save();

        bk = [["Ruskin Bond", "The room on the Roof","0140107835"],["Ruskin Bond","A Flight of Pigeons", "0-670-04927-1"],["Ruskin Bond","The Adventures of Rusty","9788185039534"],["Chetan Bhagat","Half Girlfriend","9788129135728"],["Chetan Bhagat","One Indian Girl","9781329985841"],["Chetan Bhagat","Revolution 2020","9788129118806"],
        ["R. K. Narayan","Malgudi Days","9780434450282"],["R. K. Narayan","A Horse and Two Goats","9780370014388"],["R. K. Narayan","Under the Banyan Tree and Other Stories","9788185986142"],["Arundhati Roy","The God of Small Things","9780008262303"],["Arundhati Roy","The Ministry of Utmost Happiness","9781524733155"],["Arundhati Roy","The Algebra of Infinite Justice","9780007149490"]]
        bk_iter = iter(bk)
        for i in range(12):
            abk = next(bk_iter)
            print(abk)
            abk_iter = iter(abk)
            bname = next(abk_iter)
            tauthor =  author.objects.get(name = bname)
            # print(tauthor.name)
            brecord = book(title=next(abk_iter), writtenby = tauthor, isbn = next(abk_iter), prologue = des )
            brecord.save()

    def handle(self, *args, **options):
        self.populate()
