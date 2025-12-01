package be.larsdevolder.day01;

import java.io.InputStream;
import java.util.Scanner;

public class Level2 {
    private final Scanner scanner;
    private int timesZero;
    private final Dial dial;

    Level2(InputStream inputStream) {
        scanner = new Scanner(inputStream);
        dial = new Dial();
    }

    public void parseInput() {
        while (scanner.hasNextLine()) {
            parseLine();
        }
    }

    public void parseLine() {
        int previousPosition = dial.getPosition();
        boolean passedZero = false;
        String line = scanner.nextLine();
        char direction = line.charAt(0);
        int amount = Integer.parseInt(line.substring(1));
        timesZero += amount / 100;
        switch (direction) {
            case 'L':
                dial.decreaseDial(amount);
                if (previousPosition < getDialPosition() && previousPosition != 0) {
                    passedZero = true;
                }
                break;
            case 'R':
                dial.increaseDial(amount);
                if (previousPosition > getDialPosition() && previousPosition != 0) {
                    passedZero = true;
                }
                break;
        }
        if (passedZero || getDialPosition() == 0) {
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
