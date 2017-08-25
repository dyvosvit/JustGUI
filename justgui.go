package main

import (
    "fmt"
    "log"
    "net/http"
    "encoding/json"
    "io/ioutil"
    "net"
    "sort"
    "os/exec"
)

type UserData struct {
    Balance string `json:"Balance"`
    Gain string `json:"Gain"`
    Description string `json:"Description"`
}

type UserDatas []UserData

func returnJustGUIDatas(w http.ResponseWriter, r *http.Request){

  // get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {

    balance, err := ioutil.ReadFile("MODULES/balance") // just pass the file name
    if err != nil {
        fmt.Print(err)
    }

    balance_str := string(balance) // convert  to a 'string'

    gain, err := ioutil.ReadFile("MODULES/gains_client_gain") // just pass the file name
    if err != nil {
        fmt.Print(err)
    }

    gain_str := string(gain) // convert  to a 'string'

    UserDatas := UserDatas{
        UserData{Balance: balance_str, Gain: gain_str, Description: "JustGUI Service"},
    }    
    
    json.NewEncoder(w).Encode(UserDatas)

  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }

}

func index(w http.ResponseWriter, r *http.Request){


    fmt.Fprintf(w, "Welcome to JustGUI Service!")

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)

}

func config(w http.ResponseWriter, r *http.Request) {


  // get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)

    fmt.Println(ip)
  // valide the ip address
  if string(ip) == "YOUR IP" {

    fmt.Fprintf(w, "Welcome to JustGUI Config Service!")
    system("MODULES/download.py")


  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }    
}

func shutdown(w http.ResponseWriter, r *http.Request) {

 // get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {

    fmt.Fprintf(w, "Welcome to JustGUI Shutdown Service!")
    system("MODULES/shutdown")

  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }

}

func start(w http.ResponseWriter, r *http.Request) {

 // get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {

    fmt.Fprintf(w, "Welcome to JustGUI Start Service!")
    system("MODULES/start")

  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }
    
}

func logs(w http.ResponseWriter, r *http.Request) {


// get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {

   logs, err := ioutil.ReadFile("/root/.pm2/logs/gunthy-linx64-out-0.log") // just pass the file name
    if err != nil {
        fmt.Print(err)
    }

    logs_str := string(logs) // convert Description to a 'string'

    fmt.Fprintf(w, logs_str)
    
  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }
}


func trades(w http.ResponseWriter, r *http.Request) {

// get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {
    
    trades, err := ioutil.ReadFile("MODULES/trades") // just pass the file name
    if err != nil {
        fmt.Print(err)
    }

    trades_str := string(trades) // convert Description to a 'string'

    fmt.Fprintf(w, trades_str)
    
  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }

}

func balance(w http.ResponseWriter, r *http.Request) {

// get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {
    
    balance, err := ioutil.ReadFile("MODULES/balance") // just pass the file name
    if err != nil {
        fmt.Print(err)
    }

    balance_str := string(balance) // convert Description to a 'string'

    fmt.Fprintf(w, balance_str)
    
  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }

}

func gain(w http.ResponseWriter, r *http.Request) {

// get client ip address

    ip,_,_ := net.SplitHostPort(r.RemoteAddr)

    var keys []string
    for k := range r.Header {
        keys = append(keys, k)
    }
    sort.Strings(keys)


  // valide the ip address
  if string(ip) == "YOUR IP" {
    
    gain, err := ioutil.ReadFile("MODULES/gains_client_gain") // just pass the file name
    if err != nil {
        fmt.Print(err)
    }

    gain_str := string(gain) // convert Description to a 'string'

    fmt.Fprintf(w, gain_str)
    
  }else{

    fmt.Fprintf(w, "Access Prohibited!")

  }

}


func handleRequests() {

    http.HandleFunc("/", index)
    http.HandleFunc("/all", returnJustGUIDatas)
    http.HandleFunc("/balance", balance)
    http.HandleFunc("/gain", gain)
    http.HandleFunc("/config", config)
    http.HandleFunc("/shutdown", shutdown)
    http.HandleFunc("/start", start)
    http.HandleFunc("/logs", logs)
    http.HandleFunc("/trades", trades)

    log.Fatal(http.ListenAndServe(":4523", nil))
}

func system(cmd string, arg ...string) {
    out, err := exec.Command(cmd, arg...).Output()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(out))
}

func main() {

    fmt.Println("JustGUI - v1.0")
    handleRequests()
}

