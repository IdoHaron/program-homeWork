let socket = io.connect("http://"+document.domain+':'+location.port);
 socket.on("connect", ()=>{
     socket.emit("connected");
 });
 socket.on("Ap-connection", (msg)=>{
    console.log('here'); //<!- -<script src="{{url_for('static', filename="FrontCode.js")}}"></script>-- >
    //window.prompt(msg.msg);
 });
 socket.on("Frame",(Frame)=>{
    
 });
