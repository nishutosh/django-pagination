 page=request.GET.get("page")
          limit=questions.objects.count()          
          totalpages=int(ceil(limit/10.0))
          last=limit%10         
          try: 
               page=int(page)
               if page<=limit and page >= 0:
                  currentpage=(page/10)+1               
                  queslist=questions.objects.defer("body","ucode").order_by("-views")[page:page+10] 
                  npage=page+10;
                  ppage=page-10;
               else:
                  currentpage=totalpages
                  queslist=questions.objects.defer("body","ucode").order_by("-views")[limit-last:limit]                
                  npage=10; 
                  ppage=limit-last-10;                       
          except:
              currentpage=1
              queslist=questions.objects.defer("body","ucode").order_by("-views")[0:10]             
              npage=10;  
              ppage=-10;   
          return render(request,"indexqueslist.html",{"contacts":queslist,"page":npage,"totalpages":
            totalpages,"current":currentpage,"previouspage":ppage,})            
