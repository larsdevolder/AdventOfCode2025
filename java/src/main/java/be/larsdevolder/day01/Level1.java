package be.larsdevolder.day01;

import java.io.InputStream;
import java.util.Scanner;

public class Level1 {
    private final Scanner scanner;
    private int timesZero;
    private final Dial dial;

    Level1(InputStream inputStream) {
        scanner = new Scanner(inputStream);
        dial = new Dial();
    }

    public void parseInput() {
        while (scanner.hasNextLine()) {
            parseLine();
        }
    }

    public void parseLine() {
        String line = scanner.nextLine();
        char direction = line.charAt(0);
        int amount = Integer.parseInt(line.substring(1));
        switch (direction) {
            case 'L':
                dial.decreaseDial(amount);
                break;
            case 'R':
                dial.increaseDial(amount);
                break;
        }
        if (dial.getPosition() == 0) {
            timesZero++;
        }
    }

    public int getTimesZero() {
        return timesZero;
    }

    public int getDialPosition() {
        return dial.getPosition();
    }
}
