package org.example

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    val input = readln().split(" ")
    println(rev(rev(input[0].toInt())+rev(input[1].toInt())))
}
fun rev(target:Int):Int{
         return target.toString().reversed().toInt()
}