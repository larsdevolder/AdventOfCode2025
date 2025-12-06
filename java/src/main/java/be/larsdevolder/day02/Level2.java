package be.larsdevolder.day02;

import java.io.InputStream;
import java.util.*;

public class Level2 {
    long sum;

    Level2() {
        sum = 0;
    }

    public void parseInput(InputStream inputStream) {
        try (Scanner scanner = new Scanner(inputStream)) {
            String[] line = scanner.nextLine().split(",");
            for (String range: line) {
                long start = Long.parseLong(range.split("-")[0]);
                long end = Long.parseLong(range.split("-")[1]);
                checkRange(start, end);
            }
        }
    }

    public void checkRange(long start, long end) {
        for (long index = start; index <= end; index++) {
            String number = String.valueOf(index);
            boolean isInvalid = false;
            for (int j = 1; j < number.length(); j++) {
                if (number.length() % j == 0) {
                    Set<Long> substrings = new HashSet<>();
                    for (int k = 0; k+j <= number.length(); k += j) {
                        substrings.add(Long.parseLong(number.substring(k, k+j)));
                    }
                    if (substrings.size() == 1) {
                        isInvalid = true;
                    }
                }
            }
            if (isInvalid) { sum += index; }
        }
    }

    public long getSum() {
        return sum;
    }
}
