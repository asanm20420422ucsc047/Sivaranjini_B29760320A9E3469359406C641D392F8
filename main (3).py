class Cricket

{
public static void main(String args[])throws IOException
{
int pcode,iplayed,noplayer,notout,runs;
double avg=0,avgall=0;
String name;
BufferedReader br= new BufferedReader (new InputStreamReader(System.in));
System.out.println(“Enter How many Players:=> “);
noplayer=Integer.parseInt(br.readLine());
CricketPlayer s[]=new CricketPlayer[noplayer];

for(int i=0;i<noplayer;i++)
{
System.out.println(“Enter Player Code:=> “);
pcode=Integer.parseInt(br.readLine());
System.out.println(“Enter Player Name:=> “);
name=br.readLine();
System.out.println(“Enter Runs:=> “);
runs=Integer.parseInt(br.readLine());
System.out.println(“Enter No of innings Played:=> “);
iplayed=Integer.parseInt(br.readLine());
System.out.println(“Enter No of Times Not Out:=> “);
notout=Integer.parseInt(br.readLine());
s[i]=new CricketPlayer(pcode,name,runs,iplayed,notout);
}

for(int i=0;i<noplayer;i++)
{
avg+=s[i].average(“Ram”);
}

System.out.println(“Average of Ram is :> “+avg);

for(int i=0;i<noplayer;i++)
{
avgall=s[i].average();
System.out.println(“Average of “+s[i].name+” is :>”+avgall);
}
}
}