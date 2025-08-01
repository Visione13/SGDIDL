import java.util.Arrays;

public class gameBoard {

    char[] board;

    public gameBoard(int size){
        size = size * size;
        board = new char[size];

        Arrays.fill(board, '.');
    }

    public void printBoard(){
        for (int i = 0; i < board.length; i++) {
            if(i%3==0){
                System.out.println();
            }
            System.out.print(board[i]);
        }
        System.out.println();
    }
}