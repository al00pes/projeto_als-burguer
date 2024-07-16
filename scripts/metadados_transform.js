function transform(line){
    var values = line.split(',');
    var obj = new Object();
    
    obj.DATA_VENDA = values[0];
    obj.CLIENTE_ID = values[1];
    obj.NOME_CLIENTE = values[2];
    obj.EMAIL_CLIENTE = values[3];
    obj.TELEFONE_CLIENTE = values[4];
    obj.ENDERECO_CLIENTE = values[5];
    obj.PRODUTO = values[6];
    obj.QUANTIDADE = values[7];
    obj.PRECO_UNITARIO = values[8];
    obj.PRECO_TOTAL = values[9];

    var jsonString = JSON.stringify(obj);
    return jsonString

}