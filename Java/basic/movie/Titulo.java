public class Titulo{
    private String nombre;
    private int fechaDeLanzamiento;
    private int duracionEnMinutos;
    private boolean incluidaEnElPlan;
    private double sumaDeLasEvaluaciones;
    private int totalDeEvaluaciones;

    public Titulo(String nombre, int fechaDeLanzamiento, int duracionEnMinutos, boolean incluidaEnElPlan, double sumaDeLasEvaluaciones, int totalDeEvaluaciones) {
        this.nombre = nombre;
        this.fechaDeLanzamiento = fechaDeLanzamiento;
        this.duracionEnMinutos = duracionEnMinutos;
        this.incluidaEnElPlan = incluidaEnElPlan;
        this.sumaDeLasEvaluaciones = sumaDeLasEvaluaciones;
        this.totalDeEvaluaciones = totalDeEvaluaciones;
    }

    

    public String getNombre(){
        return nombre;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public int getFechaDeLanzamiento(){
        return fechaDeLanzamiento;
    }

    public void setFechaDeLanzamiento(int fechaDeLanzamiento){
        this.fechaDeLanzamiento = fechaDeLanzamiento;
    }

    public int getDuracionEnMinutos(){
        return duracionEnMinutos;
    }

    public void setDuracionEnMinutos(int duracionEnMinutos){
        this.duracionEnMinutos = duracionEnMinutos;
    }

    public boolean getIncluidaEnElPlan(){
        return incluidaEnElPlan;
    }

    public void setIncluidaEnElPlan(boolean incluidaEnElPlan){
        this.incluidaEnElPlan = incluidaEnElPlan;
    }

    public double getSumaDeLasEvaluaciones(){
        return sumaDeLasEvaluaciones;
    }

    public void setSumaDeLasEvaluaciones(double sumaDeLasEvaluaciones){
        this.sumaDeLasEvaluaciones = sumaDeLasEvaluaciones;
    }

    public int getTotalDeEvaluaciones(){
        return totalDeEvaluaciones;
    }

    public void setTotalDeEvaluaciones(int totalDeEvaluaciones){
        this.totalDeEvaluaciones = totalDeEvaluaciones;
    }

    public void showtTechnicalSheet(){
        System.out.println("Nombre: " + nombre);
        System.out.println("Fecha de lanzamiento: " + fechaDeLanzamiento);
        System.out.println("Duración en minutos: " + duracionEnMinutos);
        System.out.println("Incluida en el plan: " + incluidaEnElPlan);
        System.out.println("Suma de las evaluaciones: " + sumaDeLasEvaluaciones);
        System.out.println("Total de evaluaciones: " + totalDeEvaluaciones);
    }

    public void assess(double note){
        sumaDeLasEvaluaciones += note; 
        totalDeEvaluaciones++;      
    }

    public double getAverage(){
        return sumaDeLasEvaluaciones / totalDeEvaluaciones;
    }

   
}