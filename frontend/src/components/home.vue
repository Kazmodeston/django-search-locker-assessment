
<template>
  <div>
    <div class="flex bg-yellow-400 -mt-16 w-full">
        <div class="w-24 mr-20"><img src="img/logo.png" alt="" class="w-full pt-3 pr-0 pb-5 pl-5"></div>
        <div class="w-3/6 mr-8">
            <ul class="flex w-full mr-8">
                <li class="mr-10 mt-9 font-semibold">Home</li>
                <li class="mr-10 mt-9 font-semibold">Find a Locker</li>
                <li class="mr-10 mt-9 font-semibold">Size Guide</li>
                <li class="mr-10 mt-9 font-semibold">Location</li>
                <li class="mr-10 mt-9 font-semibold">Help Center</li>
            </ul>
        </div>
        <div class="w-38">
            <ul class="flex w-full mr-20">
                <li class="mr-10 mt-9 font-semibold">My Account</li>
                <li class="mr-10 mt-9 font-semibold">080-188-0872</li>
                <button class="bg-yellow-300 mt-9 w-32 rounded-full text-white font-bold ">Pay Your Bill</button>
            </ul>
        </div>
    </div>
    
    <div class="bg-cover" style="background-image:url(../img/banner.jpg);">
        <div class="">
          <h1 class="text-red-600 text-medium  pt-20 font-bold text-left ml-10">Find a Locker</h1>
           </div>
           <div class="flex justify-between"> 
             <div class="w-1/2"><input type="search" placeholder="Enter City or State" name="locker" v-model="keyword" id="" class="mb-12 w-1/2 h-16 border-0 xl:mb-40 xl:w-full xl:ml-10 md:w-full md:ml-10 sm:w-full sm:ml-10"></div>
           <div>
            <h1 class="w-1/2"></h1>
           </div>
           </div>
          
       
    </div>

    
    <div class="bg-gray-600 h-14 w-full xl:flex xl:justify-between sm:justify-around">
      
      <div class="">
        <p class="pt-4 pl-4 text-xl text-white font-mono">6 Open Lockers Available</p>
      </div>
      <div class="">
        <div class="pt-3 text-md text-white font-mono mr-20">Sort By: <select name="closest" id="" class="text-black "><option value="">Closest</option><option value="lower Price">Lower Price</option></select></div> 
        <!-- <div class="pt-2 text-md ml-11 text-white"><select name="closest" id="" class="text-black"><option value="">Closest</option><option value="lower Price">Lower Price</option></select></div> -->
      </div>
      
    </div>

    <div class="flex w-full h-96  mt-8">
        <div class="h-60 bg-black ml-2 w-1/5">
            <img src="img/Screenshot_6.png" alt="" class="w-full h-full"> <br>
            <span class="text-sm text-blue-600 font-bold">22A Adeola Odeku Street, VI, <br>Lagos</span>
            <div class="flex justify-center items-center">
                <div class="flex items-center mt-2 mb-4">
                    <svg class="mx-1 w-4 h-4 fill-current text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
                    <svg class="mx-1 w-4 h-4 fill-current text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
                    <svg class="mx-1 w-4 h-4 fill-current text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
                    <svg class="mx-1 w-4 h-4 fill-current text-yellow-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
                    <svg class="mx-1 w-4 h-4 fill-current text-yellow-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
                </div>
            </div>
            <span class="text-sm text-blue-600 font-bold">0.3 Miles Away</span>
        </div>
        <div class="w-full ml-10 h-60">
            <div class="flex mt-1 mb-2 ml-10 justify-between">
                <div>
                    <select name="" id="" class="w-full" @change="onQuantity($event)" v-model="quantity">
                      <option value="Small">Small</option>
                      <option value="Medium">Medium</option>
                      <option value="Large">Large</option>
                    </select>
                </div>
                <div class="mr-60">
                    <a href="" class="text-blue-500">View the guide size</a>
                </div>
            </div>

            <div class="w-full">
                <table class="table-auto w-11/12 ml-4  font-bold">
                    <tr class="bg-gray-300 border m-10" v-for="locker in lockers" :key="locker.id">
                        <td class="w-40 text-left">{{locker.featured}}</td>
                        <td class="w-80 text-left">{{locker.price_description}}</td>
                        <td class="w-90 text-left">{{locker.locker_description}}</td>
                        <td class="w-50 text-left">{{locker.status}}</td>
                        <td class="w-30 text-left"><button class="bg-green-500 text-center text-white font-bold rounded-sm py-1 px-1 text-sm pl-8 pr-8">Rent Now</button></td>
                    </tr> <br>
                </table>
                
            </div>
            <div class="mt-2">
                    <p><span class="text-red-800">+</span> <span class="text-blue-600 text-sm">View all lockers at this Location</span></p>
                </div>
        </div>
    </div>
  </div>
</template>


<script>

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0,
      keyword: null,
      lockers: [],
      quantity: "Small"
    }
  },

  watch: {
    keyword(after, before) {
      this.getResults();
    }
  },

  methods: {
    
   getResults() {

     if(this.keyword == "")
     {

     }
     else
     {
            fetch('http://localhost:8000/api/locker-search/'+ this.keyword + "/")
            .then(response =>response.json())
            //.then(data => console.log(data))
            .then(data => this.lockers=data)
            .catch((error) => {
                console.error('Error:', error);
            });
     }

             
   },

   onQuantity(event)
   {
     //const search = event.target.value
     //console.log(this.quantity)

      if(this.quantity == "")
     {

     }
     else
     {
            fetch('http://localhost:8000/api/locker-search/'+ this.quantity + "/")
            .then(response =>response.json())
            //.then(data => console.log(data))
            .then(data => this.lockers=data)
            .catch((error) => {
                console.error('Error:', error);
            });
     }

   },

   getAllResults(){
     fetch('http://localhost:8000/api/locker-list/')
            .then(response =>response.json())
            .then(data => this.lockers=data)
            .catch((error) => {
                console.error('Error:', error);
            });
   }


  },
  created() {

        this.getAllResults()
    },

  
}
</script>
