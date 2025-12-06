package be.larsdevolder.day02;

import java.io.IOException;
import java.io.InputStream;

public class Day02 {
    public static void main(String[] args) {
        level1();
        level2();
    }

    public static void level1() {
        try (InputStream inputStream = Day02.class.getResourceAsStream("/inputs/day02/input.txt")) {
            Level1 level1 = new Level1(inputStream);
            long sum = level1.getSum();
            System.out.printf("LEVEL 1:\nSum of invalid indexes is %s\n", sum);
        } catch (NullPointerException | IOException e) {
            throw new RuntimeException("Input file could not be found or loaded.", e);
        }
    }

    public static void level2() {
        try (InputStream inputStream = Day02.class.getResourceAsStream("/inputs/day02/input.txt")) {
            Level2 level2 = new Level2();
            level2.parseInput(inputStream);
            long sum = level2.getSum();
            System.out.printf("LEVEL 2:\nSum of invalid indexes is %s\n", sum);
        } catch (NullPointerException | IOException e) {
            throw new RuntimeException("Input file could not be found or loaded.", e);
        }
    }

}
