import java.net.Socket
import java.net.SocketException
import kotlin.concurrent.thread

val clientz = Socket("197.210.44.252", 3306)
val clientOutput = clientz.getOutputStream()
val clientInput = clientz.getInputStream()
var response: String = ""

fun recvMesage() {
    val recvMsglist = mutableListOf<Char>()
    while (true) {

        var nextByte = clientInput.read()
        if (nextByte.toChar() != '.') {
            recvMsglist.add(nextByte.toChar())

        } else {

            val msg = recvMsglist.joinToString("")
            println(msg)
            response = msg
            recvMsglist.clear()
            break


        }

    }

}

fun sendMesage(mesage: String) {
    clientOutput.write(mesage.toByteArray())

}

fun sender(){
    var con = true
    while (con) {

        var input = readLine().toString()
        sendMesage(input)
        recvMesage()
        /*when (response) {
            " " -> {
                sendMesage("hi")
                recvMesage()
            }
            "hello" -> {
                sendMesage("how are you")
                recvMesage()
            }
            "am fine" -> {
                sendMesage("okay bye")
                con = false
            }


        }*/


    }
    println("closing connection with ${clientz.inetAddress.hostAddress}")
    clientz.close()
}

fun main() {
    //var response: String
    //sender()
    sendMesage("hi")
    recvMesage()
    clientz.keepAlive
}