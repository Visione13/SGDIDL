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

        while(checkWin()){
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
                    if(playerMove){
                        System.out.println("Bitte Gültige Eingabe");
                    }
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

        if(!playerMove){
            System.out.println("Du hast gewonnen!");
        }else{
            System.out.println("Du hast verloren!");
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

    private boolean checkWin(){
        for(int i = 0; i < 9; i=i+3){
            if(gb.board[i] == gb.board[i+1] && gb.board[i+1] == gb.board[i+2] && gb.board[i] != '.'){
                return false;
            }
        }
        for(int i = 0; i < 3; i++){
            if(gb.board[i] == gb.board[i+3] && gb.board[i+3] == gb.board[i+6] && gb.board[i] != '.'){
                return false;
            }
        }
        if(gb.board[0] == gb.board[4] && gb.board[4] == gb.board[8] && gb.board[0] != '.'){
            return false;
        }
        if(gb.board[2] == gb.board[4] && gb.board[4] == gb.board[6] && gb.board[2] != '.'){
            return false;
        }
        return true;
    }
}