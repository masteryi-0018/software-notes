// hello.cj

foreign func SetConsoleOutputCP(wCodePageID: UInt32): Bool

main() {
    unsafe { SetConsoleOutputCP(65001) }
    println("你好，仓颉")
}