package be.larsdevolder.day01;

import java.io.IOException;
import java.io.InputStream;
import java.util.Scanner;

public class Day01 {
    public static void main(String[] args) throws IOException {
        level1();
        System.out.println();
        level2();
    }

    public static void level1() {
        try (InputStream inputStream = Day01.class.getResourceAsStream("/inputs/day01/level1.txt")) {
            Level1 level1 = new Level1(inputStream);
            level1.parseInput();
            int timesZero = level1.getTimesZero();
            System.out.printf("LEVEL 1:\nDial ended on 0 %d times\n", timesZero);
        } catch (NullPointerException | IOException e) {
            throw new RuntimeException("Input file could not be found or loaded.", e);
        }
    }

    public static void level2() {
        try (InputStream inputStream = Day01.class.getResourceAsStream("/inputs/day01/level1.txt")) {
            Level2 level2 = new Level2(inputStream);
            level2.parseInput();
            int timesZero = level2.getTimesZero();
            System.out.printf("LEVEL 2:\nDial passed 0 %d times\n", timesZero);
        } catch (NullPointerException | IOException e) {
            throw new RuntimeException("Input file could not be found or loaded.", e);
        }
    }
}
