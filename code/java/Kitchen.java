public class Kitchen {
    // 
    public static void main(String[] args) {
        TeaKettle kettle = new TeaKettle();
        System.out.println(kettle.repr());
        kettle.boil();
        System.out.println(kettle.repr());
        kettle.pour(5);
        System.out.println(kettle.repr());
    }

}

