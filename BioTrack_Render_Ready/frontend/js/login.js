
const form=document.getElementById('loginForm');
const msg=document.getElementById('message');
document.getElementById('togglePassword').onclick=()=>{
 const p=document.getElementById('password');
 p.type=p.type==='password'?'text':'password';
};
form.addEventListener('submit', async(e)=>{
 e.preventDefault();
 const body={username:username.value.trim().toLowerCase(),password:password.value};
 const res=await fetch('/api/auth/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
 const data=await res.json().catch(()=>({}));
 if(res.ok){
  localStorage.setItem('role',data.role);
  localStorage.setItem('department',data.department);
  location.href='/dashboard';
 } else {
  msg.innerHTML=data.detail || 'Login failed';
 }
});
