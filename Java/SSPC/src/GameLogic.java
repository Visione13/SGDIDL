import java.util.Objects;
import java.util.Scanner;
import java.lang.Math;

public class GameLogic {
    Scanner sc = new Scanner(System.in);

    public void start(){
        String pc = getPlayerChoice();
        String aic = getAIChoice();
        getWinner(pc, aic);
    }

    private String getPlayerChoice(){
        Scanner sc = new Scanner(System.in);

        System.out.println("Deine Auswahl:");
        String playerChoice = sc.nextLine();

        return playerChoice.toLowerCase();
    }

    private String getAIChoice(){
        String[] choice = {"stein", "schere", "papier"};
        int rand = (int)(Math.random() * 2)+ 1;

        return choice[rand];
    }

    private void getWinner(String pc, String aic){
        if(Objects.equals(pc, aic)){
            System.out.println("Unentschieden");
        } else if (Objects.equals(pc, "schere") && Objects.equals(aic, "papier") || Objects.equals(pc, "stein") && Objects.equals(aic, "schere") || Objects.equals(pc, "papier") && Objects.equals(aic, "stein")) {
            System.out.println("Du hast gewonnen");
        }else if (Objects.equals(pc, "schere") && Objects.equals(aic, "stein") || Objects.equals(pc, "stein") && Objects.equals(aic, "papier") || Objects.equals(pc, "papier") && Objects.equals(aic, "schere")) {
            System.out.println("Du hast verloren");
        }
        System.out.println(pc+ " " +aic);
    }
}