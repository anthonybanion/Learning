package Java.basic;

public class Objects{
    String name;


public static void main(String[] args){
    Objects uno = new Objects();
    uno.name= "peru";
    
    System.out.println(uno);  //Objects@1dbd16a6 nos da la direccion de memoria
    System.out.println(uno.name);
}

}