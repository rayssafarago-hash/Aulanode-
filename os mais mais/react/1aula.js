import React from "react";
import {SafeAreaView, View, Text, StyleSheet} from "react-native";
export default function App (){
  retun(
    <SafeAreaView style={styles.safe}>
    <View style = {styles.container}>
    <Text style = {styles.title}>Bem vindo</Text>
    <Text style ={stile.subtitle}>Faça login para continuar</Text>
    </View> 
    </SafeAreaView>  
    );

}
 
 const styles = StyleSheet.create({
   safe:{
     flex: 1,
     backgroundColor: "#f6f7fb",
   },
   container:{
     flex: 1,
     padding: 16,
     justifyContent: "center",
   },
   title: {fontSize: 28,
   fontWeight: "900",},
   subtitle: {
     marginTop: 8,
     color: "#555",
   },
 });