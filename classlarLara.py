#classlar - nesne tutabilen sınıflardır.
#human:nesne, nesne içine yürüme nefes alma gibi fonksiyonlar atayacağız.
#self = this
class Human:
    name = "Halit" #default value , aşağıda human1-2.name = yazıp yeni bir isim eklemezsek bu isim alınır. 
    #built-in : constructor yani yapıcı blok alanıdır. , nesne human() üretildiği anda bu yapıcı blok (init bloğu çalışır.)
    #init : initialize dan gelir. 
    def __init__(self,name):
        self.name = name #haliti iptal et aşağıda yazılan ismi ekrana yazdır demek. yeni selfnamei name atadık gibi.
        print("Bir human instance'i üretildi. ")
    def __str__(self): #-> str: ilgili fonksiyonun geriye dönüş tipini anlatır. 
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):
        name = "Ercan"
        print(f"{self.name}: {sentence}") #selfi silmeden çalıştırınca Halit, silip çalıştırınca ercan gözükür.
        #self.walk #talkın içinde walk çağırmak istediğimizde self demeliyiz.
    def walk(self):
        print(f"{self.name} is walking..")

#instance = örnek atadık yani new'lemiş olduk.
human1 = Human("Enes")
#human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
#human2.name = "Cem"
human2.talk("Selam")
human2.walk()
print(human2)


#burda çalıştırınca talk fonksiyonu 0 positional arguments but 1 was given hatası yazıyor.
#self ekledik talk fonksiyonu içine. bundan sonra hatasız çalışır.
#self ilgili nesnenin tanımlandığı fonksiyonun kendisini temsil eder. 
#self yerine humanObject de denebilir. bir parametrenin alınması gerekiyor.
# #nesne içindeki diğer alanlara erişebilmek için self keywordü üzerinden ilerlemek gerekli. 
#self reserve bir paramtere olduğu için merhaba yazınca sentence sayesinde algıladı.


#classlar buraya kadar. 
