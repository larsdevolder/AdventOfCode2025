package be.larsdevolder.day02;

import java.io.InputStream;
import java.util.Scanner;

public class Level1 {
    long sum;

    Level1(InputStream inputStream) {
        sum = 0;

        try (Scanner scanner = new Scanner(inputStream)) {
            String[] line = scanner.nextLine().split(",");
            for (String range: line) {
                long start = Long.parseLong(range.split("-")[0]);
                long end = Long.parseLong(range.split("-")[1]);
                for (long i = start; i <= end; i++) {
                    String number = String.valueOf(i);
                    if (number.length() % 2 == 0 &&
                            number.substring(0, number.length()/2)
                            .equals(number.substring(number.length()/2))) {
                        sum += i;
                    }
                }
            }
        }
    }

    public long getSum() {
        return sum;
    }
}
