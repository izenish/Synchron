//Imagine running a dog exhibition camp, with hundreds of dogs, and you have to keep track of the names, ages, and days attended for each dog. How would you design simple, reusable software to model the dogs?
//Create a parent class for all dogs as a blueprint of information and behaviors (methods) that all dogs will have, regardless of type.
//        Create child classes to represent different subcategories of dog under the generic parent blueprint.
//        Add unique attributes and behaviors to the child classes to represent differences
//        Create objects from the child class that represent dogs within that subgroup

//https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html#:~:text=Constructors%20are%20not%20members%2C%20so,be%20invoked%20from%20the%20subclass.

public class Assignment {
    String dogName;
    int age,days;

    public Assignment(String dogName, int age, int days){
    this.dogName=dogName;
    this.age=age;
    this.days=days;
    }

}
    class Child extends Assignment{
        int lifeExpectancy;
        String Breed;

       public Child(String dogName, int age, int days,int lifeExpectancy,String Breed){
           super(dogName,age,days);
           this.lifeExpectancy=lifeExpectancy;
           this.Breed=Breed;
       }
        public void setData(String dogName,int age,int days,int lifeExpectancy,String Breed){
            this.dogName=dogName;
            this.age=age;
            this.days=days;
            this.lifeExpectancy =lifeExpectancy;
            this.Breed=Breed;
        }
        public  void showDetails(){
            System.out.println("---------DOG's DETAILS----------");
            System.out.println("       Name:"+dogName);
            System.out.println("        Age:"+age);
            System.out.println("Present For:"+days);
            System.out.println("      Breed:"+Breed);
            System.out.println("LifeExpectancy:"+lifeExpectancy);
        }

        public  static void main(String[] args){
            Child dog1=new Child("Blackly",8,7,10,"GreatDane");
            Child dog2=new Child("Miley",10,11,11,"JapaneseSpitz");
            Child dog3=new Child("Tommy",8,3,12,"Doberman");

            dog1.showDetails();
            dog2.showDetails();
            dog3.showDetails();
            dog1.setData("Blacky",9,1,7,"MixedBreed");
            dog1.showDetails();

        }

    }
