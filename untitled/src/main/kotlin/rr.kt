val test = "test,mama,more',sequence',vondoom'"

fun main() {
    listOfListGetter(test)
}

fun listOfListGetter(string: String) {
    val temp = ArrayList<String>()
    val main = mutableListOf<MutableList<String>>()

    val convertedList: List<String> = string.split(",").toList()

    for (x in convertedList) {
        if ("'" in x) {
            temp.add(x.replace("'", ""))
            main.add(temp.toMutableList())
            temp.clear()
        } else {
            temp.add(x)
        }
    }
}






