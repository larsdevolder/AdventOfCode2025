package be.larsdevolder.day02;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import static org.junit.jupiter.api.Assertions.*;


class Day02Test {

    @Test
    void checkRange() {
        String input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224," +
                "1698522-1698528,446443-446449,38593856-38593862,565653-565659," +
                "824824821-824824827,2121212118-2121212124";
        InputStream inputStream = new ByteArrayInputStream(input.getBytes());
        Level2 level2 = new Level2();
        level2.parseInput(inputStream);
        assertEquals(4174379265L, level2.getSum());
    }
}