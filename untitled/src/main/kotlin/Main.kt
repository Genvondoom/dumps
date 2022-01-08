import java.net.Socket
import kotlin.concurrent.thread

val client = Socket("127.0.1.1", 5054)
fun send(message: String): String {
    val input = client.getInputStream()
    val output = client.getOutputStream()
    val recv = mutableListOf<Char>()
    var mesg = ""
    var conn = true

    output.write(message.toByteArray())
    while (conn) {


        val nextbyte = input.read()
        if (nextbyte.toChar() != '.')
            recv.add(nextbyte.toChar())
        else {
            val msg = recv.joinToString("")
            mesg = msg
            recv.clear()
            conn = false


        }

    }
    return mesg
}

fun main() {

    println(send("login,vondoom,THimberland"))
    client.close()

}