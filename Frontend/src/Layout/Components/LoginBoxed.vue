<template>
    <div id="loginBox">
        <div class="h-100 bg-plum-plate bg-animation">
            <div class="d-flex h-100 justify-content-center align-items-center">
                <b-col md="8" class="mx-auto app-login-box">
                    <div id="title">
                        My Asset
                    </div>
                    <div class="modal-dialog w-100 mx-auto">
                        <div class="modal-content">
                            <div class="modal-body">
                                <div class="h5 modal-title text-center">
                                    <h4 class="mt-2">
                                        <div>Welcome ,</div>
                                        <span>Please sign in or sign up your account below.</span>
                                    </h4>
                                </div>
                                <b-form-group id="exampleInputGroup1"
                                              label-for="exampleInput1"
                                              description="We'll never share your email with anyone else.">
                                    <b-form-input id="exampleInput1"
                                                  type="email"
                                                  required
                                                  v-model="email"
                                                  placeholder="Enter email...">
                                    </b-form-input>
                                </b-form-group>
                                <b-form-group id="exampleInputGroup2"
                                              label-for="exampleInput2">
                                    <b-form-input id="exampleInput2"
                                                  type="password"
                                                  required
                                                  v-model="password"
                                                  placeholder="Enter password...">
                                    </b-form-input>
                                </b-form-group>
                                <div class="divider"/>
                                <h6 class="mb-0">
                                    No account?
                                    <b-button variant="primary" size="sm" @click="signUp">Sign up</b-button>
                                </h6>
                            </div>
                            <div class="modal-footer clearfix">
                                <div class="float-right">
                                    <b-button variant="primary" size="lg" @click="signInEmail">Login By Email</b-button>
                                    <b-button variant="info" size="lg" @click="signInGoogle">Login By Google</b-button>
                                </div>
                            </div>
                        </div>
                    </div>
                </b-col>
            </div>
        </div>
    </div>
</template>


<script>
    import firebase from 'firebase'
    export default {
        name: 'loginBox',
        data(){
            return{
                email:'',
                password:''
            }
        },
        methods:{
            signUp(){
                firebase.auth().createUserWithEmailAndPassword(this.email,this.password)
                    .then((user)=>{
                        alert('Sign Up success!'+user);
                        this.email=''
                        this.password=''
                    })
                    .catch((error)=>{
                        alert(error);
                    })
            },
            signInEmail(){
                firebase.auth().signInWithEmailAndPassword(this.email,this.password)
                    .then((user)=>{
                        location.replace('/')
                    })
                    .catch((error)=>{
                        alert(error);
                    })
            },
            signInGoogle(){
                var provider =new firebase.auth.GoogleAuthProvider();
                firebase.auth().languageCode='ko'

                firebase.auth().signInWithPopup(provider).then(function (result) {
                    var token=result.credential.accessToken;

                    var user=result.user;
                    if(result) location.replace('/');
                }).catch(function (error) {
                    var errorCode=error.code;
                    var errorMessage=error.message;
                    // The email of the user's account used.
                    var email = error.email;
                    // The firebase.auth.AuthCredential type that was used.
                    var credential = error.credential;
                })
            }
        }

    }
</script>

<style>
    #title{
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        color: white;
        font-family: Apple;
    }
</style>
