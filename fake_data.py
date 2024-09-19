import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TaskDRF.settings')

import django
django.setup()

###modellerimize ve django içeriklerine erişebilmek için yukarıdaki gibi module dahil etmemiz lazım 
### sıralama çok önemli



from User.models import User

from faker import Faker


def set_user():


    fake=Faker(['en_US'])


    f_name =fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name,l_name,email)
     

    # Yeni telefon kodu ve numarası oluştur
    phone_code = fake.country_calling_code()
    phone_number = fake.phone_number()


    user_check= User.objects.filter(username=u_name)
    
    while user_check.exists():
        u_name =u_name +str(random.randrange(1,99))
        user_check= User.objects.filter(username=u_name)
        
        
        
        
    user=User(
        username= u_name,
        first_name = f_name,
        last_name = l_name,
        email = email,
        phone_code=phone_code,  # Telefon kodu ekle
        phone_number=phone_number  # Telefon numarası ekle
        
        
    )
    user.set_password('mert007metin')
    user.save()
    
    

from Blog.models import Blog  # Model adınızı burada doğru şekilde belirtmelisiniz




def set_blog():
    fake=Faker(['en_US'])
    # Sahte veriler oluştur
    title = fake.sentence(nb_words=6)
    summary = fake.text(max_nb_chars=100)
    context = fake.text(max_nb_chars=500)
    category = fake.word()
    keywords = ', '.join([fake.word() for _ in range(5)])  # 5 anahtar kelime oluştur
    
    
    # Rastgele bir kullanıcı seç
    users = list(User.objects.all())
    if not users:
        raise ValueError("No users found in the database.")
    
    owner = random.choice(users)  # Rastgele bir kullanıcı seç
    # Sahte blog verisi oluştur
    blog = Blog(
        title=title,
        summary=summary,
        context=context,
        category=category,
        is_active=True,
        keywords=keywords,
        owner=User.objects.first()  # İlk kullanıcıyı al, ya da uygun bir kullanıcı seç
    )
    print(title,"-", owner.username)  # Kullanıcının kullanıcı adını yazdır
    blog.save()

# 10 adet sahte blog verisi oluştur
for _ in range(100):
    set_blog()

    
# for i in range(100):
#     set_user()