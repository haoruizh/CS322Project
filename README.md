# CS322Project
The CS 322 project repository.<br>
<script>
	table = document.createElement("table");
	tBody = document.createElement("tBody");
	for(var i=0;i<5;i++){
		tr = tBody.insertRow(i);//完全的等于下两行注释里的代码
		//tr=document.createElement("tr");
		//tBody.appendChild(tr);
		for(var j=0;j<4;j++){
			td = tr.insertCell(j);//完全的等于下两行注释里的代码
			//td = document.createElement("td");
			//tr.appendChild(td);
			td.innerHTML="列："+j+" 行："+i;
		}
	}
	table.appendChild(tBody);
	document.body.appendChild(table);
</script>
————————————————
版权声明：本文为CSDN博主「Hpluvalbe」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Hpluvalbe/article/details/92440773
<h4>Team Name:</h4> Parrot<br> 
<h4>Project Name:</h4> ParrotChat<br>
<h4>Group Member:</h4>
Haorui Zhang<br>
Jihui Sheng<br>
Ke Ma<br>
Yijing Xiao<br>
Jiangquan Li<br>
Xuanfu Huang<br>
<h4>Description</h4>
This project is about developing a chatting software with an chatbot. This project is for CS322 2020 Spring, WSU Pullman.<br>
<h5>Developing Tool and Language:</h5>
<b>Source Control:</b> github<br>
<b>Programming Language:</b> Python<br>
<b>Developing Tools:</b> Visual Studio Code<br>
