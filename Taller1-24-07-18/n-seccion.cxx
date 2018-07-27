#include <bits/stdc++.h>

using namespace std;
double nseccion(int n,double inf, double sup);
double funcion(double x);
double rec(double in,double fin,int n,double lim);
double g,m,c,t,v;
int main()
{
    int p;
    double sup,inf,r;
    cout<<" Ecuación a hallar la raiz: gm/c*(1-e^-((c/m)*t))-v\n ingrese las constantes g,m,t,v separadas por espacio o enter\n";
    cin>>g>>m>>t>>v;
    cout<<" ingrese el numero de particiones: ";
    cin>>p;
    if(p<2)
    {
        cout<<"\n las particiones no deben ser menores que 2 \n";
        return 0;
    }
    cout<<" ingrese el limite inferior( numero de "<<numeric_limits<double>::min()<<" a "<<numeric_limits<double>::max()<<"): ";
    cin>>inf;
    cout<<" ingrese el limite superior( numero de "<<numeric_limits<double>::min()<<" a "<<numeric_limits<double>::max()<<"): ";
    cin>>sup;
    if(sup<inf)
    {
        cout<<"\n el limite superior no debe ser menor que el limite inferior \n";
        return 0;
    }
    r=nseccion(p,inf,sup);
    if(r==sup+1)
        cout<<" No hay solucion ";
    else
    cout<<" la solucion es: "<<r;
    return 0;
}
double nseccion(int n,double inf, double sup)
{
    return rec(inf,sup,n,sup);
}
double funcion(double x)
{
    //cout<<" x "<<x<<" ds "<<x-2<<'\n';
    return g*m/x *(1-exp(-1*(x/m)*t))-v;
}
double rec(double in,double fin,int n,double lim)
{
    vector<double> sec;
    double part=(fin-in)/n,aux;
    sec.push_back(in);
    aux=part+in;
    for(int g=1; g<n; g++)
    {
        sec.push_back(aux);
        aux+=part;
    }
    sec.push_back(fin);

    for(int i=0; i<sec.size()-1;i++)
    {
        double res=funcion(sec[i]);

        if(abs(res)<=0.0000001)
        {
            return sec[i];
        }
        else if(res*funcion(sec[i+1])<0)
        {
            return rec(sec[i],sec[i+1],n,lim);
        }
    }
    return lim+1;
}
