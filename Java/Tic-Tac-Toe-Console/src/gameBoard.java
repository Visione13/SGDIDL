import java.util.Arrays;

public class gameBoard {

    char[][] board;

    public gameBoard(int size){
        board = new char[size][size];

        for (char[] chars : board) {
            Arrays.fill(chars, 'F');
        }
    }

    public void printBoard(){
        System.out.println("___");
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                System.out.print(board[i][j]);
            }
            System.out.println();
        }
        System.out.print("___");
    }
}