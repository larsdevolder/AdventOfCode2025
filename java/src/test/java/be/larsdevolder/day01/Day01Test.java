package be.larsdevolder.day01;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.*;

class Day01Test {
    static final String input = "L68\n" +
            "L30\n" +
            "R48\n" +
            "L5\n" +
            "R60\n" +
            "L55\n" +
            "L1\n" +
            "L99\n" +
            "R14\n" +
            "L82";

    @Test
    void level1Test() {
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        Level1 level1 = new Level1(inputStream);
        assertEquals(50, level1.getDialPosition());
        int[] expectedPositions = {82, 52, 0, 95, 55, 0, 99, 0, 14, 32};
        for (int expectedPosition: expectedPositions) {
            level1.parseLine();
            assertEquals(expectedPosition, level1.getDialPosition());
        }
        assertEquals(3, level1.getTimesZero());
    }

    @Test
    void level2Test() {
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        Level2 level2 = new Level2(inputStream);
        level2.parseInput();
        assertEquals(6, level2.getTimesZero());
    }
}