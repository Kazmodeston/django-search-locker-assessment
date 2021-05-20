<template>
  <div>
    <div class="flex bg-yellow-400">
        <div class="w-28 mr-20"><img src="img/logo.png" alt="" class="w-full pt-3 pr-0 pb-5 pl-5"></div>
        <div class="w-3/6 mr-8">
            <ul class="flex w-full mr-8">
                <li class="mr-10 mt-9 font-semibold">Home</li>
                <li class="mr-10 mt-9 font-semibold">Find a Locker</li>
                <li class="mr-10 mt-9 font-semibold">Size Guide</li>
                <li class="mr-10 mt-9 font-semibold">Location</li>
                <li class="mr-10 mt-9 font-semibold">help Center</li>
            </ul>
        </div>
        <div class="w-38">
            <ul class="flex w-full mr-20">
                <li class="mr-10 mt-9 font-semibold">My Account</li>
                <li class="mr-10 mt-9 font-semibold">080-188-0872</li>
                <button class="bg-yellow-300 mt-9 w-32 rounded-full text-white font-bold md:items-center">Pay Your Bill</button>
            </ul>
        </div>
    </div>
    <div class="bg-cover bg-center" style="background-image:url(../img/banner.jpg);">
        <h1 class="text-red-600 text-medium pl-4 pt-20 font-bold md:justify-end">Find a Locker</h1><br>
        <input type="search" placeholder="Enter City or State" name="locker" v-model="keyword" id="" class="xl:ml-4 sm:ml-10 mb-12 xl:w-1/2 sm:w-small h-16 border-0 ">
    </div>
    <div class="md:bg-secondary-200 sm:bg-red-600 lg:bg-primary xl:bg-secondary-200 h-14 w-full flex">
        <p class="pt-2 pl-4 text-xl text-white w-3/4 font-mono">6 Open Lockers Available</p>
        <div class="pt-3 text-md text-white font-mono">Sort By:</div>
        <div class="pt-2 text-md ml-11 text-white"><select name="closest" id="" class="text-black"><option value="">Closest</option><option value="lower Price">Lower Price</option></select></div>
    </div>

    <div class="flex w-full h-auto  mt-8">
        <div class="h-small bg-black ml-2 w-small">
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
        </div>
        <div class="w-large ml-10">
            <div class="flex m-10 justify-between">
                <div>
                    <select name="" id="" class="w-full"><option value="">Small</option><option value="">Medium</option><option value="">Large</option></select>
                </div>
                <div>
                    <a href="" class="text-blue-500">View the guide size</a>
                </div>
            </div>

            <div class="w-full">
                <table class="table-auto w-large ml-10 ">
                    <tr class="mb-12 bg-gray-300 px-4 py-4 border m-10 " v-for="locker in lockers" :key="locker.id">
                        <td class="w-1/5 ">{{locker.locker_name}}</td>
                        <td class="w-1/5 ">{{locker.price_description}}</td>
                        <td class="w-1/5 ">{{locker.locker_description}}</td>
                        <td class="w-1/5 ">{{locker.status}}</td>
                        <td><button class="bg-green-500 text-center text-white font-bold rounded-sm py-1 px-1 ">Rent Now</button></td>
                    </tr>
                </table>
                <div class="ml-10 mt-2">
                    <p><span class="text-red-800">+</span> <span class="text-blue-600 text-sm">View all lockers at this Location</span></p>
                </div>
            </div>
        </div>
    </div>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  </div>
</template>


<script>
//const axios = require('axios');
//import axios from 'axios';
//import axios from '../dist/axios.js'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0,
      keyword: null,
      lockers: []
    }
  },

  watch: {
    keyword(after, before) {
      this.getResults();
    }
  },

  methods: {
    /* getResults() {
            axios.get('/livesearch', { params: { keyword: this.keyword } })
                .then(res => this.lockers = res.data)
                .catch(error => {
                  console.log(error)
                });
        }, */
    
    /* getName(){
          const baseURL = "http://localhost:8000/api/"
       fetch('http://localhost:8000/api/locker-list/'+ this.keyword)
      .then(response =>{
        //return response.json()
        console.log(response.json())
      })
      //const data = res.json();
      //this.data = data;
      //console.log(res)
    }, */
    
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


  },
  created() {

        //this.getName()
    },

  
}
</script>
