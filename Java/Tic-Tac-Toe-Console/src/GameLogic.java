import java.util.Scanner;

public class GameLogic {
    gameBoard gb = new gameBoard(3);
    Scanner sc = new Scanner(System.in);
    ai ai = new ai();

    boolean ongoing = true;

    public void gameStart(){
        gb.printBoard();
        int choice;
        boolean playerMove = true;
        boolean clean;

        while(ongoing){
            clean = false;

            do {
                if(playerMove){
                    System.out.println("Welches feld besetzen?");
                    choice = sc.nextInt();
                }else{
                    choice = ai.makeMove();
                }
                if(checkValidate(choice)){
                    place(choice, playerMove);
                    clean = true;
                }else{
                    System.out.println("Bitte Gültige Eingabe");
                }
            }
            while(!clean);
            gb.printBoard();
            if(playerMove){
                playerMove = false;
            }else{
                playerMove = true;
            }
        }
    }

    public void place(int x, boolean playerMove){
        if(playerMove){
            gb.board[x-1] = 'X';
        }else{
            gb.board[x-1] = 'O';
        }
    }

    private boolean checkValidate(int x){
        return gb.board[x-1] == '.';
    }
}