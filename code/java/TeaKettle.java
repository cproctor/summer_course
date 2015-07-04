// TeaKettle.java
// --------------
// by Chris Proctor
// This is a Java reimplementation of the TeaKettle class we wrote in Python.

public class TeaKettle {

    public String repr() {
        return "A kettle with " + water_level + " units of " + temp + " water.";
    }

    public void boil() {
        temp = "hot";
        if (water_level > 0) {
            water_level -= 1;
        } 
        else {
            System.out.println("Fire!");
        }
    }

    public void throw_at(String target) {
        System.out.println("Haha, threw the kettle at " + target);
        water_level = 0;
    }

    public void fill() {
        water_level = 10;
    }

    public int pour(int amount) {
        if (amount <= water_level) {
            System.out.println("Poured out " + amount + " units of " + temp + " water.");
            water_level -= amount;
            return amount;
        }
        else {
            System.out.println(
                "Even though " + amount + 
                " was requested, could only pour out " + 
                water_level + " units of water."
            );
            int water_available = water_level;
            water_level = 0;
            return water_available;
        }
    }

    private String temp = "cold";
    private int water_level = 10;
}
