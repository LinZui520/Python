package thread;

public class Person extends Thread {

    public static int sum = 0;

    public String name;

    public Person(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        for(int i = 0; i < 10000; i++){


//            synchronized(Person.class){
//                Person.sum ++;
//            }

            Person.sum ++;
        }
    }

    public static void main(String[] args) {
        Person LinZui = new Person("LinZui");
        Person ZhuGui = new Person("ZhuGui");
        Person Jack = new Person("Jack");

        LinZui.start();
        ZhuGui.start();
        Jack.start();

        try {
            sleep(3000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }


        System.out.println(Person.sum);
    }
}
