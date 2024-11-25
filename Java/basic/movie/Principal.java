 public class Principal{
 public static void main(String[] arg){
        Titulo titulo1 = new Titulo("The Witcher", 2019, 60, true,0, 0);
        titulo1.assess(5);
        titulo1.assess(4);
        titulo1.assess(3);
        
        titulo1.showtTechnicalSheet();
        System.out.println("Promedio: " + titulo1.getAverage());
        System.out.println("Total de Evaluaciones: " + titulo1.getTotalDeEvaluaciones());

    }
}