import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

void hello() {
  print("Hello World");
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: GridView.count(
          crossAxisCount: 3,
          children: <Widget>[
            ElevatedButton(
              onPressed: (){},
              child: Text("1"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
              ),
            ElevatedButton(
              onPressed: (){},
              child: Text("2"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
            ElevatedButton(
              onPressed: (){},
              child: Text("3"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
            ElevatedButton(
              onPressed: (){},
              child: Text("4"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ), 
            ElevatedButton(
              onPressed: (){},
              child: Text("5"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
            ElevatedButton(
              onPressed: (){},
              child: Text("6"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
            ElevatedButton(
              onPressed: (){},
              child: Text("7"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
            ElevatedButton(
              onPressed: (){},
              child: Text("8"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
            ElevatedButton(
              onPressed: (){},
              child: Text("9"),
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadiusDirectional.circular(1),
                ),
              ),
            ),
          ],
        )
      ),
    );
  }
}