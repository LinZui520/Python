package thread;

public class Person extends Thread {

    public String name;

    public Person(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        for(int i = 0; i < 10; i++){
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println(this.name + " is running" + i);
        }
    }

    public static void main(String[] args) {
        Person LinZui = new Person("LinZui");
        Person ZhuGui = new Person("ZhuGui");
        LinZui.start();
        ZhuGui.start();
    }
}
