import org.hyunjun.school.*;
import java.util.List;
import java.util.Calendar;

/*
How to compile this java file
javac -cp foodAPI.jar Food.java

How to run this java file
java -cp .:./foodAPI.jar Food
However Windows should use ; instead of :

*/

public class Food {
    public static void main(String[] args) throws SchoolException {
        // get api of kmla
        School api = new School(School.Type.HIGH, School.Region.KANGWON, "K100000414");

        // get today's calendar
        Calendar cal = Calendar.getInstance();
        // get this year
        int year = cal.get(Calendar.YEAR);

        List<SchoolMenu> menu; // variable to store monthly menus

        /*
        integer array to store the number of days in a certain month
        Month: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
        Index: 0   1   2   3   4   5   6   7   8   9   10  11
        */
        int[] dayArr = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // change value of february if this year is leap year, cause duh
        if (isLeapYear(cal)) dayArr[1] = 29;

        // start i: starting month
        // end i: ending month
        for (int month = 1; month <= 12; month++) {
            /*
            M[num]: start of day [num]
            D[num]: start of day [num]
            b: start of breakfast
            l: start of lunch
            d: start of dinner
            */
            System.out.println("M" + month);
            menu = api.getMonthlyMenu(year, month);
            int days = dayArr[month - 1];

            for (int j = 1; j <= days; j++) {
                System.out.println("D" + j);

                System.out.println("b");
                System.out.println(menu.get(j - 1).breakfast);

                System.out.println("l");
                System.out.println(menu.get(j - 1).lunch);

                System.out.println("d");
                System.out.println(menu.get(j - 1).dinner);
            }
        }
    }

    public static boolean isLeapYear(Calendar c) {
        return c.getActualMaximum(Calendar.DAY_OF_YEAR) > 365;
    }
}
