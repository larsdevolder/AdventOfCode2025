package be.larsdevolder.day01;

public class Dial {
    private int position;

    Dial() {
        position = 50;
    }

    public void increaseDial(int amount) {
        position += amount;
        position %= 100;
    }

    public void  decreaseDial(int amount) {
        position -= amount;
        while (position < 0) {
            position += 100;
        }
        position %= 100;
    }

    public int getPosition() {
        return position;
    }
}
